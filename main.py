import asyncio
from dotenv import load_dotenv
import os

# 导入必要的autogen组件
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

# 加载环境变量
load_dotenv()

async def main():
    # 配置职位信息
    job_position = "Software Engineer"
    
    # 初始化模型客户端
    model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY"),
        timeout=20
    )

    # 创建面试官角色
    interviewer = AssistantAgent(
        name="Interviewer",
        model_client=model_client,
        system_message=f'''
        你是{job_position}职位的专业面试官。每次只问一个清晰的问题并等待回答。
        总共问3个问题，涵盖技术能力、问题解决能力和文化适应性。
        问完3个问题后，在面试结束时说'TERMINATE'。每个问题控制在50字以内。
        '''
    )

    # 创建候选人角色（由用户扮演）
    candidate = UserProxyAgent(
        name="Candidate",
        input_func=input,  # 接收用户输入作为候选人回答
    )

    # 创建职业教练角色
    career_coach = AssistantAgent(
        name="Career Coach",
        model_client=model_client,
        system_message=f'''
        你是{job_position}面试的职业教练。对候选人的回答提供建设性反馈和改进建议。
        面试结束后，总结候选人表现并提供可操作的建议。内容控制在100字以内。
        '''
    )

    # 设置面试终止条件
    termination = TextMentionTermination("TERMINATE")

    # 创建面试团队
    interview_team = RoundRobinGroupChat(
        participants=[interviewer, candidate, career_coach],
        termination_condition=termination,
        max_turns=20
    )

    # 开始面试流程
    print(f"=== {job_position} 面试开始 ===")
    async for message in interview_team.run_stream(task="开始面试，提出第一个问题"):
        print("-" * 70)
        print(f"{message.source}: {message.content}")

if __name__ == "__main__":
    asyncio.run(main())
