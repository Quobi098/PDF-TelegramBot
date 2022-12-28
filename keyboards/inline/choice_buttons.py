from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ru_choice = InlineKeyboardMarkup(row_width=1,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="✅ Да",
                                          callback_data='Eng'
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="❌ Нет",
                                          callback_data='cancel_choice_ru'
                                      )
                                  ]
                              ])

eng_choice = InlineKeyboardMarkup(row_width=1,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="✅ Yes",
                                          callback_data='Ru'
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="❌ No",
                                          callback_data='cancel_choice_eng'
                                      )
                                  ]
                              ])