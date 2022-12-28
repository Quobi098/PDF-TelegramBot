from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

ru_menu = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text="🔍 Найти слово в PDF файле",
                                                            callback_data='find_word')
                                   ],
                                   [
                                       InlineKeyboardButton(text="ℹ Информация о файле",
                                                            callback_data='about_file')
                                   ],
                                   [
                                       InlineKeyboardButton(text="🗣 Изменить язык",
                                                            callback_data='choose_lang_ru')
                                   ],
                                   [
                                       InlineKeyboardButton(text="❌ Отмена",
                                                            callback_data='cancel')
                                   ]
                               ])

eng_menu = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text="🔍 Find word in PDF file",
                                                       callback_data='find_word')
                                    ],
                                    [
                                        InlineKeyboardButton(text="ℹ Information about file",
                                                       callback_data='about_file')
                                    ],
                                    [
                                        InlineKeyboardButton(text="🗣 Change language",
                                                       callback_data='change_lang_eng')
                                    ],
                                    [
                                        InlineKeyboardButton(text="❌ Cancel",
                                                       callback_data='cancel')
                                    ]
                                ])
