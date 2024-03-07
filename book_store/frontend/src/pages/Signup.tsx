import React, { useState } from "react";
import axios from "axios";
import * as bases from "../components/bases";

const RegistrationForm: React.FC = () => {
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [country, setCountry] = useState("");
  const [phone, setPhone] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [agreeTerms, setAgreeTerms] = useState(false);
  const [error, setError] = useState("");
  const [registrationSuccess, setRegistrationSuccess] = useState(false);

  const emailRegex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i;
  const phoneRegex = /^\d{10}$/;
  const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/;

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (
      !firstName ||
      !lastName ||
      !country ||
      !phone ||
      !email ||
      !password ||
      !confirmPassword
    ) {
      setError("Пожалуйста, заполните все обязательные поля.");
      return;
    }

    if (!emailRegex.test(email)) {
      setError("Пожалуйста, введите корректный адрес электронной почты.");
      return;
    }

    if (!phoneRegex.test(phone)) {
      setError("Пожалуйста, введите корректный номер телефона (10 цифр).");
      return;
    }

    if (!passwordRegex.test(password)) {
      setError("Пожалуйста, введите пароль согласно требованиям.");
      return;
    }

    if (password !== confirmPassword) {
      setError("Пароли не совпадают. Пожалуйста, повторите ввод.");
      return;
    }

    if (!agreeTerms) {
      setError("Необходимо согласиться с условиями и положениями.");
      return;
    }

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/user/register/",
        {
          firstName,
          lastName,
          country,
          phone,
          email,
          password,
        },
      );
      console.log("Успешно зарегистрирован", response.data);
      setRegistrationSuccess(true); // Устанавливаем флаг успешной регистрации
      // Перезагружаем страницу через 2 секунды
      setTimeout(() => {
        window.location.reload();
      }, 2000);
    } catch (error) {
      console.error("Ошибка при регистрации", error);
      setError("Ошибка при регистрации. Пожалуйста, попробуйте еще раз.");
    }
  };

  const toggleShowPassword = () => {
    setShowPassword(!showPassword);
  };

  const toggleShowConfirmPassword = () => {
    setShowConfirmPassword(!showConfirmPassword);
  };

  return (
    <bases.Base1>
      <div className="bg-dark text-secondary px-4 py-5 text-center w-50 m-5 p-5">
        <main className="form-signin w-100 m-auto">
          <form onSubmit={handleSubmit}>
            <h1 className="h3 mb-3 fw-normal">Пожалуйста, зарегистрируйтесь</h1>

            <div className="form-floating">
              <input
                type="text"
                className="form-control"
                id="firstName"
                placeholder="Имя"
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
              />
              <label htmlFor="firstName">Имя</label>
            </div>

            <div className="form-floating">
              <input
                type="text"
                className="form-control"
                id="lastName"
                placeholder="Фамилия"
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
              />
              <label htmlFor="lastName">Фамилия</label>
            </div>

            <div className="form-floating">
              <select
                className="form-select"
                id="country"
                value={country}
                onChange={(e) => setCountry(e.target.value)}
              >
                <option value="">Выберите страну</option>
                <option value="Казахстан">Казахстан</option>
                <option value="США">США</option>
                <option value="Канада">Канада</option>
                <option value="Россия">Россия</option>
                <option value="Евросоюз">Евросоюз</option>
                <option value="Другое">Другое</option>
              </select>
              <label htmlFor="country">Страна</label>
            </div>

            <div className="form-floating">
              <input
                type="tel"
                className="form-control"
                id="phone"
                placeholder="Телефонный номер"
                value={phone}
                onChange={(e) => setPhone(e.target.value)}
              />
              <label htmlFor="phone">Телефонный номер</label>
            </div>

            <div className="form-floating">
              <input
                type="email"
                className="form-control"
                id="email"
                placeholder="name@example.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
              <label htmlFor="email">Адрес электронной почты</label>
            </div>

            <div className="form-floating">
              <input
                type={showPassword ? "text" : "password"}
                className="form-control"
                id="password"
                placeholder="Пароль"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
              <label htmlFor="password">Пароль</label>
              <span
                className="eye-icon"
                onClick={toggleShowPassword}
                style={{
                  cursor: "pointer",
                  position: "absolute",
                  right: "10px",
                  top: "40%",
                  transform: "translateY(-50%)",
                }}
              >
                {showPassword ? "👁️" : "👁️"}
              </span>
            </div>

            <div className="form-floating">
              <input
                type={showConfirmPassword ? "text" : "password"}
                className="form-control"
                id="confirmPassword"
                placeholder="Повторите пароль"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
              />
              <label htmlFor="confirmPassword">Повторите пароль</label>
              <span
                className="eye-icon"
                onClick={toggleShowConfirmPassword}
                style={{
                  cursor: "pointer",
                  position: "absolute",
                  right: "10px",
                  top: "40%",
                  transform: "translateY(-50%)",
                }}
              >
                {showConfirmPassword ? "👁️" : "👁️"}
              </span>
            </div>

            <div className="form-check text-start my-3">
              <input
                className="form-check-input"
                type="checkbox"
                id="agreeTerms"
                checked={agreeTerms}
                onChange={(e) => setAgreeTerms(e.target.checked)}
                required
              />
              <label className="form-check-label" htmlFor="agreeTerms">
                Я соглашаюсь с условиями и положениями
              </label>
            </div>

            {error && <p className="text-danger">{error}</p>}
            {registrationSuccess && (
              <p className="text-success">Вы успешно зарегистрированы.</p>
            )}

            <button className="btn btn-primary w-100 py-2" type="submit">
              Зарегистрироваться
            </button>
            <p className="mt-5 mb-3 text-body-secondary">© 2017–2023</p>
          </form>
        </main>
      </div>
    </bases.Base1>
  );
};

export default RegistrationForm;
