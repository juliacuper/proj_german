from django.shortcuts import render
from django.core.cache import cache
from . import terms_work


def index(request):
    """Главная страница веб-сервиса."""
    return render(request, "index.html")


def terms_list(request):
    """Список терминов для изучения немецкого языка."""
    terms = terms_work.get_terms_for_table()
    return render(request, "term_list.html", context={"terms": terms})


def add_term(request):
    """Форма для добавления нового термина."""
    return render(request, "term_add.html")


def send_term(request):
    """Обработка отправки нового термина и его определения."""
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        
        # Проверка корректности введенных данных
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым."
        elif len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым."
        else:
            context["success"] = True
            context["comment"] = "Ваш термин успешно принят!"
            terms_work.write_term(new_term, new_definition)
        
        if context["success"]:
            context["success-title"] = "Успех!"
        else:
            context["success-title"] = "Ошибка!"
        
        return render(request, "term_request.html", context)
    
    # Если метод не POST, перенаправляем на страницу добавления термина
    return add_term(request)


def show_stats(request):
    """Показ статистики по терминам."""
    stats = terms_work.get_terms_stats()
    return render(request, "stats.html", {"stats": stats})
