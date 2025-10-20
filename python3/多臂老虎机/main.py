# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : main.py
@Time    : 2024/9/16 17:02
@Author  : Echo Wang
'''

import numpy as np


class MultiArmedBandit:
    def __init__(self, num_arms, rewards_mean, rewards_std):
        """
        初始化多臂老虎机
        :param num_arms: 臂的数量
        :param rewards_mean: 每个臂的平均奖励（列表或数组）
        :param rewards_std: 每个臂的奖励标准差（列表或数组）
        """
        self.num_arms = num_arms
        self.rewards_mean = np.array(rewards_mean)
        self.rewards_std = np.array(rewards_std)
        self.counts = np.zeros(num_arms)  # 每个臂被选择的次数
        self.values = np.zeros(num_arms)  # 每个臂的平均奖励

    def pull_arm(self, arm):
        """
        拉一个臂，并返回奖励
        :param arm: 要拉的臂的索引
        :return: 从该臂获得的奖励
        """
        reward = np.random.normal(self.rewards_mean[arm], self.rewards_std[arm])
        self.counts[arm] += 1
        self.values[arm] += (reward - self.values[arm]) / self.counts[arm]  # 更新平均奖励
        return reward

    def select_arm_ucb(self, total_pulls, exploration_factor=2.0):
        """
        使用UCB算法选择臂
        :param total_pulls: 总共的拉臂次数
        :param exploration_factor: 探索因子，用于调整置信区间的宽度
        :return: 要拉的臂的索引
        """
        ucb_values = self.values + exploration_factor * np.sqrt(np.log(total_pulls + 1) / (self.counts + 1e-9))
        return np.argmax(ucb_values)

    # 示例用法


if __name__ == "__main__":
    num_arms = 4
    rewards_mean = [0, 1, 2, 0.5]
    rewards_std = [1, 1.5, 1, 1]

    bandit = MultiArmedBandit(num_arms, rewards_mean, rewards_std)

    total_pulls = 10
    cumulative_rewards = 0

    for i in range(total_pulls):
        chosen_arm = bandit.select_arm_ucb(i)
        reward = bandit.pull_arm(chosen_arm)
        cumulative_rewards += reward

        print(f"Pull {i + 1}/{total_pulls}, Arm {chosen_arm}, Reward: {reward}")

    print(f"Total cumulative reward: {cumulative_rewards}")