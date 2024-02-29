import pathlib

current_dir = pathlib.Path(__file__).parent


def get_cats_info(path):

    try:
        with open(current_dir / "cats_file.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            cats = []
            
            for line in lines:
                line = line.strip().split(',')
                cats_info = {
                    "id": line[0],
                    "name": line[1],
                    "age": line[2]
                }
                cats.append(cats_info)
                
            return cats
                
    except FileNotFoundError:
        return "Не вдалося знайти файл."

get_cats_info("current_dir/salary_file.txt")

cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)