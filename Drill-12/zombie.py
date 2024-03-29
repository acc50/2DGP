import random
import math
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
from pico2d import *
import main_state

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10


animation_names = ['Attack', 'Dead', 'Idle', 'Walk']


class Zombie:
    images = None

    def load_images(self):
        self.font = load_font('ENCR10B.TTF', 16)
        if Zombie.images == None:
            Zombie.images = {}
            for name in animation_names:
                Zombie.images[name] = [load_image("./zombiefiles/female/"+ name + " (%d)" % i + ".png") for i in range(1, 11)]

    def __init__(self):
        # positions for origin at top, left
        balls = main_state.get_balls()
        ball_positions = []
        for ball in balls:
            ball_positions.append((ball.x, ball.y))

        positions = [(43, 750), (1118, 750), (1050, 530), (575, 220), (235, 33), (575, 220), (1050, 530), (1118, 750)]
        self.patrol_positions = []
        for p in ball_positions:
            self.patrol_positions.append((p[0], 1024 - p[1]))  # convert for origin at bottom, left
        self.patrol_order = 1
        self.target_x, self.target_y = None, None
        self.x, self.y = self.patrol_positions[0]

        self.load_images()
        self.dir = random.random()*2*math.pi # random moving direction
        self.speed = 0
        self.timer = 1.0  # change direction every 1 sec when wandering
        self.frame = 0

        self.hp = 100
        self.damage = 5

        self.build_behavior_tree()

    def calculate_current_position(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(50, self.x, 1280 - 50)
        self.y = clamp(50, self.y, 1024 - 50)

    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()
        self.timer -= game_framework.frame_time
        if self.timer < 0:
            self.timer += 1.0
            self.dir = random.random() * 2 * math.pi

        return BehaviorTree.SUCCESS

        pass

    def check_balls(self):
        balls = main_state.get_balls()
        if len(balls) <= 0:     # 공이 남아있지 않으면
            return BehaviorTree.SUCCESS     # 성공
            pass
        else:
            return BehaviorTree.FAIL
            pass
        pass
    
    def find_big_balls(self):       # 큰 공 주변에 있는지 검사
        big_balls = main_state.get_big_balls()
        distance = 0
        # 큰 공이 존재하면
        if len(big_balls) < 0:
            return BehaviorTree.FAIL

        else:
            for ball in big_balls:
                distance = (ball.x - self.x) ** 2 + (ball.y - self.y) ** 2
                if distance < (PIXEL_PER_METER * 10) ** 2:
                    self.dir = math.atan2(ball.y - self.y, ball.x - self.x)
                    return BehaviorTree.SUCCESS

            # 큰공 전부 검사 시 근처에 X
            self.speed = 0
            return BehaviorTree.FAIL

        pass

    def find_small_balls(self):       # 작은 공 주변에 있는지 검사
        small_balls = main_state.get_small_balls()
        distance = 0
        # 큰 공이 존재하면
        if len(small_balls) < 0:
            return BehaviorTree.FAIL

        else:
            for ball in small_balls:
                distance = (ball.x - self.x) ** 2 + (ball.y - self.y) ** 2
                if distance < (PIXEL_PER_METER * 10) ** 2:
                    self.dir = math.atan2(ball.y - self.y, ball.x - self.x)
                    return BehaviorTree.SUCCESS

            # 작은공 전부 검사 시 근처에 X
            self.speed = 0
            return BehaviorTree.FAIL

        pass

    def move_to_big_ball(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()
        return BehaviorTree.SUCCESS

    def move_to_small_ball(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()
        return BehaviorTree.SUCCESS

    def find_player(self):      # 탐색
        boy = main_state.get_boy()
        distance = (boy.x - self.x) ** 2 + (boy.y - self.y) ** 2
        if distance < (PIXEL_PER_METER * 10) ** 2:
            self.dir = math.atan2(boy.y - self.y, boy.x - self.x)
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL
        pass

    def move_to_player(self):       #  플레이어로 이동
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()
        return BehaviorTree.SUCCESS
        pass

    def build_behavior_tree(self):
        wander_node = LeafNode("Wander", self.wander)
        find_player_node = LeafNode("Find Player", self.find_player)
        move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        move_to_small_ball_node = LeafNode("Move to Small Ball", self.move_to_small_ball())
        move_to_big_ball_node = LeafNode("Move to Big Ball", self.move_to_big_ball())
        find_big_ball_node = LeafNode("Find Big Ball", self.find_big_balls())
        find_small_ball_node = LeafNode("Find Small Ball", self.find_small_balls())
        check_balls_node = LeafNode("Check Balls",self.check_balls())

        chase_node = SequenceNode("Chase")      # 추적
        chase_node.add_children(find_player_node, move_to_player_node)

        check_chase_node = SequenceNode("CheckChase")       # 추적 확인
        check_chase_node.add_children(check_balls_node, chase_node)

        wander_chase_node = SelectorNode("WanderChase")
        wander_chase_node.add_children(chase_node, wander_node)
        self.bt = BehaviorTree(wander_chase_node)
        pass




    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        self.bt.run()
        pass


    def draw(self):
        draw_rectangle(*self.get_bb())
        self.font.draw(self.x - 40, self.y + 50, '(HP: %d)' % self.hp, (255, 255, 0))

        if math.cos(self.dir) < 0:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
        else:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].draw(self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].draw(self.x, self.y, 100, 100)


    def handle_event(self, event):
        pass

