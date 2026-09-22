from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()


llm = OpenAI()

#result = llm("Write a very very short poem")

#print(result)

code_prompt = PromptTemplate(
    input_variables=["language", "task"],
    template="Write a very short {language} function that will {task}"
)

code_chain = LLMChain(
    llm=llm, prompt=code_prompt
    )

result = code_chain({
    "language":"python", 
    "task":"return a list of numbers"
    })

print(result["text"])