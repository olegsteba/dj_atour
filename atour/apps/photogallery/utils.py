class DataMixin:
    paginate_by = 3 #Построничный вывод
    
    def get_user_context(self, **kwargs):
        """Формируем контекст для вывода"""
        context = kwargs
        return context