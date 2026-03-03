# **ML Assignment — Q‑Learning (DQN) Quadcopter**

2D 刚体物理下的四旋翼控制项目。本分支仅保留 Human 与本人训练的 DQN 模型，并将其接入 Balloon 游戏用于展示。

<p align="center">
  <img src="media/balloon.gif" alt="Main Game" width="50%"/>
</p>

目标是在限定时间内控制无人机触碰尽可能多的气球（Balloon 模式）。

当前包含的玩家：

- **Human**：方向键手动控制推进器
- **DQN（本人训练）**：离散动作空间（保持 5 帧），基于 stable-baselines3 训练并集成到主游戏

环境与智能体的原理介绍可参考原项目作者论文：[Reinforcement_Learning_for_the_Control_of_Quadcopters.pdf](Reinforcement_Learning_for_the_Control_of_Quadcopters.pdf)。

项目开发记录（原作者）：
<p align="center">
  <a href="https://youtu.be/J1hv0MJghag" target="_blank">
    <img src="media/thumb.png" alt="Youtube Devlog" width="50%"/>
  </a>
</p>

仓库仍包含 Snowglobe 模式（鼠标控制）：

<p align="center">
  <img src="media/snowglobe.gif" alt="Snowglobe" width="50%"/>
</p>

## 使用方式（从源码运行）

推荐在 conda 虚拟环境（例如 `game`，Python 3.8）下运行，并使用 VS Code 将解释器指向 `/Applications/anaconda3/envs/game/bin/python`。

安装依赖：

```bash
python -m pip install -r requirements.txt
```

运行 Balloon 游戏（Human + DQN）：

```bash
python -m quadai
```

说明：
- Human 用方向键控制
- DQN 自动决策，动作保持 5 帧（与训练一致）
- 游戏时长 40 秒，右上角显示倒计时

Snowglobe 模式：

```bash
python -m quadai snowglobe
```

## 更换/更新 DQN 模型

默认加载路径：`src/quadai/DQN/models/rl_model_v0_5000000_steps.zip`。如需替换为你的新模型：
- 将新模型放入上述目录，并保持文件名一致；或
- 修改 `src/quadai/player.py` 中 `DQNPlayer` 的 `model_path`

## 致谢
- 本项目在原仓库基础上定制，仅保留 Human 与 DQN 展示，移除 SAC 与 PID 在主游戏中的展示：  
  https://github.com/AlexandreSajus/Quadcopter-AI
- 环境/算法细节参考原作者论文与视频。
