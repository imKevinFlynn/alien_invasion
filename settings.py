
class Settings:
    """Класс для хранения всех настроек игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        # параметры окна
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (134, 143, 175)  # цвет фона

        # настройки пришельцев
        self.alien_speed = 15.5  # скорость пришельцев
        self.fleet_drop_speed = 10  # уменьшение высоты флота при достижении края экрана.
        self.fleet_direction = 1  # (значение 1 это движение пришельцев право, -1 влево)

        # настройки корабля
        self.ship_speed = 2  # скорость корабля.
        self.ship_limit = 3  # лимит доступных кораблей.

        # параметры снарядов корабля
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 3
        self.bullet_color = (60, 60, 60)
