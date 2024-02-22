import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import Login from "../pages/Login";
import Signup from "../pages/Signup";
import About from "../pages/About";
import FAQs from "../pages/FAQs";
// import Login from "../pages/Login";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path={""} element={<Home />}></Route>
        <Route path={"login/"} element={<Login />}></Route>
        <Route path={"sign-up/"} element={<Signup />}></Route>
        <Route path={"about/"} element={<About />}></Route>
        <Route path={"faqs/"} element={<FAQs />}></Route>
        <Route path={"*"} element={<Home />}></Route>
      </Routes>
    </BrowserRouter>
  );
}
