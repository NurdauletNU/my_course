import React, { useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import * as bases from "../components/bases";

const LoginPage: React.FC = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!email.trim() || !password.trim()) {
      setError("Please fill in all fields");
      return;
    }

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/token/", {
        email,
        password,
      });

      console.log("Успешно вошел", response.data);
      // Добавьте необходимые действия после успешного входа
    } catch (error) {
      console.error("Ошибка при входе", error);
      setError("Ошибка при входе. Пожалуйста, проверьте свои учетные данные.");
    }
  };

  return (
    <bases.Base1>
      <div className="bg-dark text-secondary px-4 py-5 text-center w-50 m-5 p-5">
        <main className="form-signin w-100 m-auto">
          <form onSubmit={handleSubmit}>
            <img
              className="mb-4"
              src="https://getbootstrap.com/docs/5.3/assets/brand/bootstrap-logo.svg"
              alt=""
              width="72"
              height="57"
            />
            <h1 className="h3 mb-3 fw-normal">Welcome back!</h1>

            {error && <div className="alert alert-danger">{error}</div>}

            <div className="form-floating">
              <input
                type="email"
                className="form-control"
                id="floatingInput"
                placeholder="name@example.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
              <label htmlFor="floatingInput">Email address</label>
            </div>
            <div className="form-floating">
              <input
                type={showPassword ? "text" : "password"}
                className="form-control"
                id="floatingPassword"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
              <label htmlFor="floatingPassword">Password</label>
              <span
                className="password-toggle bi bi-eye"
                onClick={togglePasswordVisibility}
                style={{
                  cursor: "pointer",
                  position: "absolute",
                  right: "10px",
                  top: "40%",
                }}
              >
                {showPassword ? "Hide" : "Show"}
              </span>
            </div>

            <div className="form-check text-start my-3">
              <input
                className="form-check-input"
                type="checkbox"
                value="remember-me"
                id="flexCheckDefault"
              />
              <label className="form-check-label" htmlFor="flexCheckDefault">
                Remember me
              </label>
            </div>
            <button className="btn btn-primary w-100 py-2" type="submit">
              Log in
            </button>
            <p className="mt-5 mb-3 text-body-secondary">© 2017–2023</p>
          </form>
          <p className="mt-3">
            Don't have an account yet? <Link to="/sign-up">Sign up</Link>
          </p>
        </main>
      </div>
    </bases.Base1>
  );
};

export default LoginPage;
