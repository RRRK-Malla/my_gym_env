import sys
import numpy as np
import math
import random

import gym
import drive_car

def gameRun():
    global epsilon, epsilon_decay
    for episode in range(MAX_EPISODES):

        # Init environment
        state = env.reset()
        total_reward = 0

        # AI tries up to MAX_TRY times
        for t in range(MAX_TRY):

            # In the beginning, do random action to learn
            if random.uniform(0, 1) < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(val[state])

            # Do action and get result
            next_state, reward, done, _ = env.step(action)
            total_reward += reward

            # Get correspond q value from state, action pair
            q_value = val[state][action]
            best_q = np.max(val[next_state])

            # Q(state, action) <- (1 - a)Q(state, action) + a(reward + rmaxQ(next state, all actions))
            val[state][action] = (1 - learning_rate) * q_value + learning_rate * (reward + gamma * best_q)

            # Set up for the next iteration
            state = next_state

            # Draw games
            env.render()

            # When episode is done, print reward
            if done or t >= MAX_TRY - 1:
                print("Episode %d finished after %i time steps with total reward = %f." % (episode, t, total_reward))
                break

        # exploring rate decay
        if epsilon >= 0.005:
            epsilon *= epsilon_decay


if __name__ == "__main__":
    env = gym.make("Drivezy-v0")
    MAX_EPISODES = 5555
    MAX_TRY = 100
    epsilon = 1
    epsilon_decay = 0.9
    learning_rate = 0.1
    gamma = 0.6
    num_box = tuple((env.observation_space.high + np.ones(env.observation_space.shape)).astype(int))
    val = np.zeros(num_box + (env.action_space.n,))
    gameRun()
