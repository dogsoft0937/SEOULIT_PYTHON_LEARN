camille={
    'attack_damage':60,
    'attack_speed':0.625,
    'armor':26
}
camille.update(attack_speed=0.999)
print(camille)
camille.clear()
print(camille)

mydict={'math':100,'english':50}

print(mydict.get('math'))
print(mydict.get('twice','No twice'))