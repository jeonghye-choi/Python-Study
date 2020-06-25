class Unit(object):
    def __init__(self, rank, size, life):
        self.name = self.__class__.__name__
        self.rank = rank
        self.size = size
        self.life = life
    def show_status(self):
        print('이름: {}'.format(self.name))
        print('등급: {}'.format(self.rank))
        print('사이즈: {}'.format(self.size))
        print('라이프: {}'.format(self.life))

class Goblin(Unit):
    def __init__(self, rank, size, life, attack_type, damage):
        super(Goblin, self).__init__(rank, size, life)
        self.attack_type = attack_type
        self.damage = damage

    def show_status(self):
        super(Goblin, self).show_status()
        print('공격 타입: {}'.format(self.attack_type))
        print ('데미지: {}'.format(self.damage))

    def attack(self):
        print('[{}]이 공격합니다! 상대방 데미지({})'.format(self.name, self.damage))
        
class SphereGoblin(Goblin):
    def __init__(self, rank, size, life, attack_type, damage, sphere_type):
        super(SphereGoblin, self).__init__(rank, size, life, attack_type, damage)
        self.sphere_type = sphere_type
    def show_status(self):
        super(SphereGoblin, self).show_status()
        print('창 타입: {}'.format(self.sphere_type))

class Hero(Unit):
    def __init__(self, rank, size, life, goblins=None):
        super(Hero, self).__init__(rank, size, life)
        if goblins is None:
            self.goblins = []
        else:
            self.goblins = goblins
    def show_own_goblins(self):
        num_of_goblins = len([x for x in self.goblins if isinstance(x, Goblin)])
        num_of_sphere_goblins = len([x for x in self.goblins if isinstance(x, SphereGoblin)])
        print('현재 영웅이 소유한 고블린은 {}명, 창 고블린은 {}명입니다.'.format(num_of_goblins, num_of_sphere_goblins))

    def make_goblins_attack(self):
        for goblin in self.goblins:
            goblin.attack()

    def add_goblins(self, new_goblins):
        for goblin in new_goblins:
            if goblin not in self.goblins:
                self.goblins.append(goblin)
            else:
                print('이미 추가된 고블린입니다.')
    def remove_goblins(self, old_goblins):
        for goblin in old_goblins:
            try:
                self.goblins.remove(goblin)
            except:
                print('소유하고 있지 않은 고블린입니다')

if __name__ == '__main__':
    # 고블린 오브젝트 생성
    goblin_1 = Goblin('병사', 'Small', 100, '근접 공격', 10)
    goblin_2 = Goblin('병사', 'Small', 100, '근접 공격', 10)
    sphere_goblin_1 = SphereGoblin('병사', 'Small', 100, '레인지 공격', 10, '긴 창')

    # 영웅 오브젝트 생성 후, 고블린 오브젝트 할당
    hero_1 = Hero('영웅', 'Big', 300, [goblin_1, goblin_2, sphere_goblin_1])
    hero_1.show_own_goblins()
    hero_1.make_goblins_attack()

    # 새로운 고블린 생성
    goblin_3 = Goblin('병사', 'Small', 100, '근접 공격', 20)
    sphere_goblin_2 = SphereGoblin('병사', 'Small', 100, '레인지 공격', 5, '긴 창')

    print('# 새로운 고블린 추가 전')
    hero_1.show_own_goblins()
    hero_1.make_goblins_attack()

    # 새로운 고블린 추가
    hero_1.add_goblins([goblin_3, sphere_goblin_2])

    print('\n# 새로운 고블린 추가 후')
    hero_1.show_own_goblins()
    hero_1.make_goblins_attack()

    # 추가한 고블린 삭제
    hero_1.remove_goblins([goblin_3, sphere_goblin_2])

    print('\n# 추가한 고블린 삭제 후')
    hero_1.show_own_goblins()
    hero_1.make_goblins_attack()

    # 영웅에게 소유되지 않은 고블린 생성
    goblin_4 = Goblin('병사', 'Small', 100, '근접 공격', 20)

    # 이미 소유한 고블린 추가
    print('\n# 에러 메세지 발생')
    hero_1.add_goblins([goblin_1])
    hero_1.remove_goblins([goblin_4])
