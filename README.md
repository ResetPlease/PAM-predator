# PAM-predator
ИНСТРУМЕНТ PAM-Predator для нахождения PAM в геноме бактериофага.(находится в разработке)

Скрипты написаны на высокоуровневом языке программирования Python версии 3 с использованием дополнительной программы 
для выравнивания нуклеотидных последовательностей "mafft" https://mafft.cbrc.jp/alignment/software/.

Все тесты проводились на компьютерах с системой Windows 10.

Алгоритм нахождения PAM: 
	1.Обработка полученных данных(spacer, геномы бактериофагов)
	2.Выравнивание последовательностей.
	3.Выделение протоспейсеров и их правых и левых примыкающих частей. (на данный момент)
	4.Анализ с помощью нейронной сети основанной на архитектуре "Перцептрон" (планируется)
	5.Визуализация.

Инструкция по применению:

!!!Все входные файлы должны находиться в одном каталоге со скриптами.!!!

!!!В начале инструмент предложит установить программу для выравнивания последовательностей "mafft". 
Чтобы инструмент заработал,ее нужно установить!!!

	Программа требует на вход: 
		1.Название файла содержащего спейсерную последовательность в формате ".txt"
		2.Название 10 файлов содержащих геномы бактериофагов в формате ".fasta" (если нет 10,то просто используйте Enter)
		
	Выходные файлы-правые и левые части примыкающие к протоспейсеру. В последовательностях(не во всех) есть PAM-мотив:
		1.Right-содержит в себе правые примыкающие к протоспейсеру части
		2.Left-содержит в себе левые примыкающие к протоспейсеру части

Исключения:
	1.Если загрузка mafft прервалась,то уже скачанный файл нужно удалить.
 	2.Модуль mafft может заинтересовать антивирус,т.к в нем содержатся исполняемые файлы.
	3.Может появиться проблема связанная с кодировкой,в этом случае нужно из главного скрипта "main.py" удалить вывод "логотипа".
	
