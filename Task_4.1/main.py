import pathlib

current_dir = pathlib.Path(__file__).parent


def total_salary(path):

    try:
        with open(current_dir / "salary_file.txt", "r", encoding="utf-8") as file:
            
            lines = file.readlines()

            total = 0
            num = len(lines)

            for line in lines:
                _, salary = line.split(',')
                total += int(salary)
            
            average = int(total / num)

            return total, average
                
    except FileNotFoundError:
        return "Не вдалося знайти файл."

total_salary("current_dir/salary_file.txt")
      
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
