from transformers import AutoModelForCausalLM, AutoTokenizer
import time
from agent import Agent
from llm import LLM

if __name__ == "__main__" :
    llm = LLM()
    agent1 = Agent(llm=llm,prompt_system="""Je suis une calculatrice qui repond le résultat du
                                            calcul uniquement avec le résultat du calcul sans 
                                            autres information. Exemple : Combien font 3 x 8 ? <sortie> 2)""")
    agent2 = Agent(llm=llm,prompt_system="""Je suis une llm qui repond en donnant une inforamtion cultivante 
                                            en incluante la valeur numérique en entrée du prompt user
                                            Exemple : entrée : 1993. La première Ligue des champîons de la France
                                            a été gagné cette année la, par l'Olympique de Marseille avec un but 
                                            de la légende du club Basile Boli. Ne parle pas uniquement de foot. 
                                            Tu peux parler de n'importe quel fait que tu trouves cultivant.
                                            Faune, Flore, Santé, Politique ...""")
    agent3 = Agent(llm=llm,prompt_system="""Donne une note sur 10 de la réponse. Etablis une grille de critère 
                                            d'abord et détermine une note sur 10""")
    question = input("Question\n")

    print("=========DEMARRAGE TIMER=========")

    start = time.time()
    print("=========AGENT 1=========")
    response = agent1.run(question)
    print(response)
    
    print("=========AGENT 2=========")
    response = agent2.run(response)
    print(response)

    print("=========AGENT 3=========")
    response = agent3.run(response)
    print(response)
    
    end = time.time()
    print(f"Temps d'exécution : {end - start:.4f} secondes")
    