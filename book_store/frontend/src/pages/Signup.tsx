import * as bases from "../components/bases";

export default function Page() {
  return (
    <bases.Base1>
      <div className="bg-dark text-secondary px-4 py-5 text-center w-50 m-5 p-5">
        <main className="form-signin w-100 m-auto">
          <form>
            <img
              className="mb-4"
              src="https://getbootstrap.com/docs/5.3/assets/brand/bootstrap-logo.svg"
              alt=""
              width="72"
              height="57"
            />
            <h1 className="h3 mb-3 fw-normal">Пожалуйста, зарегистрируйтесь</h1>

            <div className="form-floating">
              <input
                type="text"
                className="form-control"
                id="firstName"
                placeholder="Имя"
              />
              <label htmlFor="firstName">Имя</label>
            </div>

            <div className="form-floating">
              <input
                type="text"
                className="form-control"
                id="lastName"
                placeholder="Фамилия"
              />
              <label htmlFor="lastName">Фамилия</label>
            </div>

            <div className="form-floating">
              <select className="form-select" id="country">
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
              />
              <label htmlFor="phone">Телефонный номер</label>
            </div>

            <div className="form-floating">
              <input
                type="email"
                className="form-control"
                id="email"
                placeholder="name@example.com"
              />
              <label htmlFor="email">Адрес электронной почты</label>
            </div>

            <div className="form-floating">
              <input
                type="password"
                className="form-control"
                id="password"
                placeholder="Пароль"
              />
              <label htmlFor="password">Пароль</label>
            </div>

            <div className="form-check text-start my-3">
              <input
                className="form-check-input"
                type="checkbox"
                value="agree-terms"
                id="agreeTerms"
              />
              <label className="form-check-label" htmlFor="agreeTerms">
                Я соглашаюсь с условиями и положениями
              </label>
            </div>
            <button className="btn btn-primary w-100 py-2" type="submit">
              Зарегистрироваться
            </button>
            <p className="mt-5 mb-3 text-body-secondary">© 2017–2023</p>
          </form>
        </main>
      </div>
    </bases.Base1>
  );
}
