import React from "react";
import * as bases from "../components/bases";

export default function RegistrationPage() {
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
            <h1 className="h3 mb-3 fw-normal">Please sign up</h1>

            <div className="form-floating">
              <input
                type="email"
                className="form-control"
                id="floatingInput"
                placeholder="name@example.com"
              />
              <label htmlFor="floatingInput">Email address</label>
            </div>
            <div className="form-floating">
              <input
                type="password"
                className="form-control"
                id="floatingPassword"
                placeholder="Password"
              />
              <label htmlFor="floatingPassword">Password</label>
            </div>

            <div className="form-check text-start my-3">
              <input
                className="form-check-input"
                type="checkbox"
                value="agree-terms"
                id="agreeTerms"
              />
              <label className="form-check-label" htmlFor="agreeTerms">
                I agree to the terms and conditions
              </label>
            </div>
            <button className="btn btn-primary w-100 py-2" type="submit">
              Sign up
            </button>
            <p className="mt-5 mb-3 text-body-secondary">© 2017–2023</p>
          </form>
        </main>
      </div>
    </bases.Base1>
  );
}
