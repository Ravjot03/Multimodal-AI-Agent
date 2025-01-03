from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

#import os
#from dotenv import load_dotenv
#load_dotenv()
api_key = "my-groq-api"

websearchagent = Agent(
    name='webagent',
    role='search the web for the information',
    model=Groq(id = 'llama-3.3-70b-versatile', api_key=api_key),
    tools = [DuckDuckGo()],
    instructions = ['Always include sources'],
    show_tools_calls = True,
    markdown = True,
)

finagent = Agent(
    name = 'finagent',
    model=Groq(id='llama-3.3-70b-versatile', api_key=api_key),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions = 'use tables to display the data',
    shows_tools_calls = True,
    markdown=True,
)

multiagent = Agent(
    team=[websearchagent, finagent],
    model=Groq(id = 'llama-3.3-70b-versatile', api_key=api_key),
    instructions = ['Always include sources','use tables to display the data'],
    show_tools_calls=True,
    markdown=True,
)

multiagent.print_response('Summarize analyst recommendations and share the latest news for TESLA stock', stream=True)