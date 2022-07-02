import random
import sys
from pip._vendor.distlib.compat import raw_input


class RandomWord(object):
    """ Kelimeyi text filedan oku ve rastgele bir kelime return et """
    word1 = []
    def __init__(self, filename):
        self.word2 = self.word1
        with open(filename, encoding='utf8') as f:
            letters = ['î', 'û', 'â', 'a', 'b', 'c', 'ç', 'd', 'e','f','g',
                       'ğ', 'h', 'i', 'ı', 'j', 'k', 'l', 'm','n','o', 'ö',
                       'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z', 'w']
            for line in f:
                for i, c in enumerate(line):
                    if c not in letters:
                        self.word2.append(line[:i])
                        self.word2.append(len(line[:i]))
                        break
            print("\n*** Adam Asmaca ***\n")
            option = raw_input("Oyun hakkinda bilgi ister misin? e/h: ")

            if option.lower() == "e":
                print("\nKurallar\n"
                      "harf sayisini belirle\n"
                      "kime karsi oynayacagini sec\n"
                      "Tahmin etmeye basla, dikkati ol 10 hakkin var\n")
            self.userinput=input("Harf sayısını belirliyorum: ")
            self.userinput=int(self.userinput)
            self.word=self.randomchoice(self.userinput)


    def listToDict(self,lst):
        """ harf sayisi icin listi dicte cevir """
        op = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
        return op


    def randomchoice(self,b):
        """ rastgele kelime icin __init__ fonksiyonuna yardimci fonksiyon """
        self.a = self.listToDict(self.word1)
        for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]:
            v = [k for k, v in self.a.items() if v == i]
            c = random.randrange(len(v))
            item = v[c]
            if b == i:
                return item

    def display(self, guessed_letters_list):
        """ Dogru tahmin edilen harfler ile kelimeyi gostermek icin """

        word_to_display = ""
        for letter in self.word:
            if letter in guessed_letters_list:
                word_to_display += " " + letter + " "

            else:
                word_to_display += " _ "
        print("Kelimenin durumu:", word_to_display, "\n")
        return word_to_display

class Hangman(object):

    HANGMAN_PICS = ["1", "2", "3", "4", "5", "6","7", "8", "9", "10"]

    def __init__(self):
        self.hangman = self.HANGMAN_PICS[0]

    def draw(self, num_incorrect_guesses_made):
        """ Oyuncunun yaptığı yanlış tahminlerin sayısına göre tahmin hakkini goster"""
        self.hangman = self.HANGMAN_PICS[num_incorrect_guesses_made]
        print(self.hangman)

        if num_incorrect_guesses_made == 10:
            print("Kaybettin")


class Game(object):

    WRONG_ANSWER_PUTDOWNS = ["yanlis harf secimi"]

    def __init__(self, filename):
        self.secret_word = RandomWord(filename)
        self.hangman = Hangman()
        self.num_incorrect_guesses_made = 0
        self.guessed_letters = []

    def play(self):
        """ oyunun ana fonsiyonu """
        print("Adam asmacaya baslayalim!\n")
        ans=True;
        while ans:
            print(""" 
            1.bilgisayar
            2.insan
            3.cikis
            """)
            ans=input("Kimin kelimeyi belirleyecegini secin: ")
            if ans=="1":
                # Initialize the number of incorrect guesses made to 0
                while self.num_incorrect_guesses_made < 9:
                    if len(self.guessed_letters) == 0:
                        self.secret_word.display(self.guessed_letters)

                    letter_guess = raw_input("harf tahmin et: ").lower()

                    # Don't let them guess a non-alpha letter.
                    while letter_guess.isalpha() is False:
                        letter_guess = raw_input("lutfen harf girip girmediginize dikkat edin: ").lower()

                    # Once a valid letter is chosen, add it to guessed_letters
                    if letter_guess not in self.guessed_letters:
                        self.guessed_letters.append(letter_guess)


                        if letter_guess not in self.secret_word.word:
                            print(random.choice(self.WRONG_ANSWER_PUTDOWNS))
                            self.num_incorrect_guesses_made += 1
                            self.hangman.draw(self.num_incorrect_guesses_made)


                        else:
                            print("Dogru harf secimi \n")
                            self.hangman.draw(self.num_incorrect_guesses_made)


                    else:
                        print("'%s' harfi zaten sectiniz, lutfrn yeni bir harf deneyin." % letter_guess)


                    current_word = self.secret_word.display(self.guessed_letters)

                    print("Secilmis olan harfler: ", self.guessed_letters)

                    if "_" not in current_word:
                        print("Tebrikler kazandin")
                        sys.exit()
            elif ans == "2":
                print("kisi")
                answerlist = []
                answer = input('kelime gir: ')
                if len(answer) > 1 and answer.isalpha():
                    answerlist.append(answer)
                    answer = list(answerlist[0])
                    display = []
                    used = []
                    used.extend(display)
                    display.extend(answer)
                    used.extend(display)
                    for i in range(len(display)):
                        display[i] = '_ '
                    print(''.join(display))
                    print()
                    count = 0
                    incorrect = 10
                    while count < len(answer) and incorrect > 0:
                        guess = input('Harf tahmini: ')
                        guess = guess.lower()
                        print(count)

                        for i in range(len(answer)):
                            if answer[i] == guess and guess in used:
                                display[i] = guess
                                count = count + 1
                                used.remove(guess)
                        if guess not in display:
                            incorrect = incorrect - 1
                            print('yanlis tahmin', incorrect, ' hakkin kaldi')
                        print('dogru tahmin', count)
                        print(incorrect, 'hakkin kaldi')
                        print(''.join(display))
                    if count == len(answer):
                        print('kelimeyi bildin')
                        print('kelime: ',''.join(answer))
                    else:
                        print('Kaybettin')
                else:
                    print('kelime yazman gerekiyor')

            elif ans == "3":
                break
            else:
                print("Gecersiz sayi girildi. Lutfen gecerli sayi secin")

game = Game("words.txt")
game.play()