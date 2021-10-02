#include <iostream>
usin namespace std;
int main() {
    // правильные данные
    string correct_login = "Zodiac123";
    string correct_password = "123456qwerty";

    string login, password;
    // данные вводимые пользователем
    cout << "введите логин" << endl;
    cin >> login;
    cout << "введите пароль" << endl;
    cin >> password
    // сверяю данные, введенные пользователем, с правильными данными
    if ((login == correct_login) && (password == correct_password)) {
        cout << "Доступ разрешен!" << endl;
                         cout << "gjfhkgjh" << endl;  // отступ не имеет никакого значения
    } else {  // иначе
        cout << "Доступ запрещен!" << endl;
    }


    return 0;
}
