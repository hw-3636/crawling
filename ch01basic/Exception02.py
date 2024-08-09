# p. 16
def girl_friend_check(find_name):
    girl_friend = ['은하', '소원', '유주', '예린', '신비', '엄지']
    is_member = find_name in girl_friend

    if is_member:
        print('\'%s\'님은 여자 친구 멤버입니다.' % find_name)
    else:
        raise Exception('\'%s\'님은 여자 친구 멤버가 아닙니다.' % find_name)


name = ('IM')
try:
    girl_friend_check(name)
except Exception as e:
    print('예외 발생 : {}'.format(e))
