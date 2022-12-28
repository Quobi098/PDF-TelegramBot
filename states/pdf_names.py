from aiogram.dispatcher.filters.state import StatesGroup, State


class Pdf_names(StatesGroup):
    file_name = State()