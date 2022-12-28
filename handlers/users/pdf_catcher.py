from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.default import ru_menu, eng_menu
from keyboards.inline.choice_buttons import ru_choice, eng_choice
from loader import dp
from states import Pdf_names

from utils.misc.pdf import about_pdf


@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
@dp.message_handler(state=Pdf_names.file_name)
async def catch_doc(message: types.Message, state: FSMContext):
    file_name = str(message.document.file_name)
    for i in file_name:
        if i == " " or i == "«" or i == "»" or i == "," or i == ":" or i == ";" or i == "'" or i == "-":
            i = '_'
    await message.document.download(destination=file_name)
    await state.update_data(answer1=str(file_name))
    await message.reply("Документ скачан")
    await message.answer("Выберите опцию из меню ниже", reply_markup=ru_menu)


@dp.callback_query_handler(text="choose_lang_ru")
async def choose_lang(call: CallbackQuery):
    await call.answer(cache_time=10)
    await call.message.answer("Желаете сменить язык на Английский?", reply_markup=ru_choice)
    await call.message.delete()


@dp.callback_query_handler(text="change_lang_eng")
async def choose_lang(call: CallbackQuery):
    await call.answer(cache_time=10)
    await call.message.answer("Want to change language to Russian?", reply_markup=eng_choice)
    await call.message.delete()


@dp.callback_query_handler(text='Ru')
async def eng_find_button(call: CallbackQuery):
    await call.answer(cache_time=10)
    await call.message.answer("<b>Выбранный язык: Русский</b>"
                              "\n Выберите опцию из меню ниже", reply_markup=ru_menu)
    await call.message.delete()


@dp.callback_query_handler(text='Eng')
async def eng_find_button(call: CallbackQuery):
    await call.answer(cache_time=10)
    await call.message.answer("<b>Chosen language: English</b>"
                              "\n Select an option from the menu below", reply_markup=eng_menu)
    await call.message.delete()


@dp.callback_query_handler(text='cancel_choice_ru')
async def eng_find_button(call: CallbackQuery):
    await call.answer(cache_time=10)
    await call.message.answer("Команда отмена принята."
                              "\n Выберите опцию из меню ниже", reply_markup=ru_menu)
    await call.message.delete()

@dp.callback_query_handler(text='cancel_choice_eng')
async def eng_find_button(call: CallbackQuery):
    await call.answer(cache_time=10)
    await call.message.answer("Cancel order accepted."
                              "\n Select an option from the menu below", reply_markup=eng_menu)
    await call.message.delete()


@dp.callback_query_handler(text='about_file')
@dp.message_handler(state=Pdf_names.file_name)
async def about_file(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    file_name = data.get('answer1')
    file = "C:/Users/user/PycharmProjects/PDF_TelegramBot/"+f"{file_name}"
    pdf_info = about_pdf(file)
    await call.message.reply(pdf_info)
    await state.finish()
    await call.message.delete()