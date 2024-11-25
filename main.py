import db_func
import render


def main():
    db_func.create_db()
    render.render()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'')

