'''
Factory Pattern
Acest pattern ne permite sa creăm un obiect dintr-o clasa folosind o alta clasa (fabrica). Fabrica are posibilitatea de a crea obiecte din mai multe clase (de obicei aceste clase sunt siblings, adica mostenesc de la acelasi parinte).


Vom implementa următoarele clase:
English/French/Spanish Translator – clase care știu sa traduca cuvinte din română în limba specificata
translations va fi un dicționar cu acele cuvinte, exemplu `{ “masina”: “car” }` – se poate hardcoda în clasa
localize va fi o funcție care pentru un parametru de intrare, ne va da traducerea lui în acea limba (exemplu `input(“masina”)` returneaza “car”)

TranslatorFactory – clasa care are o singura metoda (preferabil statica sau de clasa) numita get_translator(language) – in functie de parametrul language, returnează un translator object.


factory = TranslatorFactory()

english_trans = factory.get_translator('en')
spanish_trans = factory.get_translator('es')

print(f'In engleza zicem {english_trans.localize("masina")}')
print(f'In spaniola zicem {spanish_trans.localize("masina")}')
'''


class EnglishTranslator:
    translations = {"masina": "car", "carte": "book"}

    def localize(self, word):
        return self.translations[word]


class FrenchTranslator:
    translations = {"masina": "voiture", "carte": "livre"}

    def localize(self, word):
        return self.translations[word]


class SpanishTranslator:
    translations = {"masina": "coche", "carte": "libro"}

    def localize(self, word):
        return self.translations[word]


class TranslatorFactory:
    @staticmethod
    def get_translator(language):
        if language == 'en':
            return EnglishTranslator()

        elif language == 'fr':
            return FrenchTranslator()

        elif language == 'es':
            return SpanishTranslator()


english_translator = TranslatorFactory.get_translator('en')
spanish_translator = TranslatorFactory.get_translator('es')
french_translator = TranslatorFactory.get_translator('fr')

print(f'In engleza zicem {english_translator.localize("masina")}')
print(f'In spaniola zicem {spanish_translator.localize("masina")}')
print(f'In franceza zicem {french_translator.localize("masina")}')
