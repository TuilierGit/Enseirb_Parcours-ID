
import openai


def get_invariant_sentence_from_response(answer):
    return answer['choices'][0]['text']


def get_invariant_from_invariant_sentence(chaine):
    chaine = chaine.strip()
    chaine = chaine.split(":")
    
    if chaine[0] == "//@ loop invariant mask":
        return chaine[1].strip()


class model:

    def __init__(self, model_type):
        self._temperature = 0.2
        self._max_tokens = 500
        self.model_type = model_type


    def ask_my_model(self, prompt,number_of_answers=1,model = None, mt = None,temp = None):

        if (model == None):
            model = self.model_type
        
        if (mt == None):
            mt = self._max_tokens

        if (temp == None):
            temp = self._temperature

        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=mt,
            temperature=temp,
            #top_p=0.95, # limite la somme cumulative des probabilités des tokens 
            n=number_of_answers, # nombre de réponse
            echo=False, # est ce qu'on ecrit la question dans la réponse
            stream=False #  détermine si les résultats doivent être retournés en entier ou s'ils doivent être diffusés en continu.
        )
        return response


    def response_with_short_prompt(self, program,number_of_answers=1 ):
        GPT_Prompt = "Compute a loop invariant for the following program!\n" + program,
        return self.ask_my_model(GPT_Prompt,number_of_answers)


    def response_with_long_prompt(self , program,number_of_answers=1 ):
        GPT_Prompt = "Compute a loop invariant for the annotated loop including [invariant] in the following C code. Please use the format of ACSL annotations and always end your response with //@ loop invariant mask : X ; where X is the computed invariant.\n\n" + program,
        return self.ask_my_model(GPT_Prompt,number_of_answers)