def main():
    import sys

    # Диэлектрические проницаемости некоторых материалов
    dielectric_map = {
        "вакуум": 1.0,
        "воздух": 1.00059,
        "стекло": 5.0,
        "вода": 80.0
    }

    # Ввод данных
    print("Программа для расчёта параметров плоского конденсатора.\n")
    try:
        U = float(input("Введите напряжение на конденсаторе U (В): "))
        d = float(input("Введите расстояние между пластинами d (м): "))
        A = float(input("Введите площадь пластин A (м^2): "))
        dielectric_input = input(
            "Введите тип диэлектрика (например: вакуум, воздух, стекло, вода): "
        ).strip().lower()

        connected_input = input(
            "Остаётся ли конденсатор подключённым к источнику? (да/нет): "
        ).strip().lower()

    except ValueError:
        print("Ошибка ввода. Убедитесь, что вы вводите числа в правильном формате.")
        sys.exit(1)

    # Проверяем наличие введённого диэлектрика в словаре
    if dielectric_input not in dielectric_map:
        print(
            f"Неизвестный диэлектрик '{dielectric_input}'. "
            f"Используйте одно из: {list(dielectric_map.keys())}"
        )
        sys.exit(1)

    # Константы
    EPS0 = 8.8541878128e-12  # Ф/м

    # Ищем диэлектрическую проницаемость
    epsilon_r = dielectric_map[dielectric_input]

    # Ёмкость без диэлектрика
    C0 = EPS0 * A / d

    # Заряд и напряжённость без диэлектрика (до введения диэлектрика)
    Q0 = C0 * U
    E0 = U / d

    # Вычисляем новую ёмкость с учётом диэлектрика
    C = epsilon_r * C0

    # Логика, зависящая от подключения к источнику
    if connected_input == "да":
        # Конденсатор остаётся подключённым → U не меняется
        U_new = U
        Q_new = C * U_new  # заряд изменится
        E_new = U_new / d  # напряжённость

        print("\nРезультаты (конденсатор подключён к источнику):")
        print(f"  - Ёмкость C  = {C:.4e} Ф")
        print(f"  - Заряд Q    = {Q_new:.4e} Кл")
        print(f"  - Поле E     = {E_new:.4e} В/м")

    else:
        # Конденсатор отключается → Q не меняется (равен Q0), меняется U
        Q_new = Q0
        U_new = Q_new / C  # новое напряжение
        E_new = U_new / d  # новая напряжённость

        print("\nРезультаты (конденсатор отключён от источника):")
        print(f"  - Ёмкость C  = {C:.4e} Ф")
        print(f"  - Заряд Q    = {Q_new:.4e} Кл (не изменился)")
        print(f"  - Новое U    = {U_new:.4e} В")
        print(f"  - Поле E     = {E_new:.4e} В/м")

    # Дополнительно выведем начальные параметры (без учёта диэлектрика)
    print("\n(Для справки) Начальные параметры без диэлектрика:")
    print(f"  - C0 = {C0:.4e} Ф")
    print(f"  - Q0 = {Q0:.4e} Кл")
    print(f"  - E0 = {E0:.4e} В/м")


if __name__ == "__main__":
    main()
