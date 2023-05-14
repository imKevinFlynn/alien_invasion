
class Settings:
    """Класс для хранения всех настроек игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        # параметры окна
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (134, 143, 175)  # цвет фона
        self.ship_speed = 1.5  # скорость корабля
        # параметры снарядов корабля
        self.bullet_speed = 0.95
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 3
        self.bullet_color = (60, 60, 60)
