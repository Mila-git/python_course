text = ("Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium,"
" totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta"
"sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, "
"sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. "
"Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, "
"sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem."
" Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, "
"nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate"
" velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")
# не обов"язково передавати стрічку в круглих дужках
# можна просто виконати text = "some text..."

# бажано додати текст, котрий описує що ми отримуємо
# також класно розділяти логічні блоки в коді порожньою стрічкою
print('Кількість символів в тексті:')
print(len(text))

# з цим завданням є момент, треба було видалити останнє слово, котре не поміщається повність
#(Необхідно видалити останнє слово, якщо воно не буде виведено повністю.)
print('Перші 120 символів:')
print(text[:121] + "...")

print('Кількість символів без пробілів:')
print(len(text) - text.count(" "))

# в цьому коді щось пішло не так, адже результат 861, при тому, що к-сть символів 864
# також добре було б спростити контрукцію на 29 стрічці
print('Кількість речень:')
print(sum(map(len, text.split("."))))

#ось варіант, як можна було б зробити:
# однак у нас ще є знаки питання і можуть бути знаки оклику
# тому можна, як варіант зробити заміну цих знаків, на крапку

# перетворюємо ? та ! в крапку та отримуємо список речень (стрічок розділених крапкою)
sentences = text.replace('?', '.')\
                .replace('!', '.')\
                .split('.')
# прибераємо можливі порожні речення
sentences = [string for string in sentences if len(string) != 0]
# отримуємо кількість речень
sentencesCount = len(sentences)
print(sentences)
print(sentencesCount)
# результат 5 речень