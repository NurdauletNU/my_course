import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link, useParams } from "react-router-dom";
import * as bases from "../components/bases";

export default function BookDetail() {
  const params = useParams();
  console.log(params);
  return <bases.Base1>something</bases.Base1>;
}
