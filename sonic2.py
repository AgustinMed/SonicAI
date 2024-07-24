import retro

env = retro.make('SonicTheHedgehog2-Genesis', 'EmeraldHillZone.Act1')

env.reset()

done = False

while not done:
    env.render() #renderiza la ventana con el juego

    #action = env.action_space.sample()
    action = [0,0,1,0,0,0,0, 1,1,1,0,0] #ir a la derecha
    #print(action) #botones de la sega genesis, se imprimen todo el tiempo 

    ob , rew, done, info = env.step(action)

    #ob -> imagen de la pantalla
    #rew -> cantidad de recompensa dependiendo del scenario.json (conseguir anillos)
    #done -> si terminó, como por ejemplo perder todas las vidas

    print("Recompensa ", rew)
    # print("Info ", info)

    
