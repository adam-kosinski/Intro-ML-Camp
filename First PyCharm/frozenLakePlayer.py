import gym
env = gym.make('FrozenLake-v0')
# env.reset()
env.render()
# print(env.action_space)
env.reset()

score = 0

for x in range(10000):
    env.reset()
    for _ in range(100):
        obs, rew, done, info = env.step(1)
        obs, rew, done, info = env.step(2)
        obs, rew, done, info = env.step(2)
        obs, rew, done, info = env.step(1)
        if done:
            if rew == 1:
                score += rew
            #else:
                # print("Loser.")
            break

print(score)