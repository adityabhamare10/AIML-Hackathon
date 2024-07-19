import express from "express";
import path from "path";
import { fileURLToPath } from "url";
import {exec} from 'child_process';
import cors from 'cors';
const app = express();

app.use(cors(
  {
    origin: '*'
  }
));
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

app.set("view engine", "ejs");
app.use(express.static("public"));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));
app.use("/assets", express.static("assets"));

app.get("/", (req, res) => {
  res.render("home");
});
app.get("/form", (req, res) => {
  res.render("index");
});


app.post("/predict-model", (req, res) => {
  const { name, age, income, home, employmentLength, intent, loanAmount, interestRate } = req.body;

  if (!name || !age || !income || !home || !employmentLength || !intent || !loanAmount || !interestRate) {
    let error = "All fields are required.";
    return res.render("index", { error });
  }

  const loan = {
    name,
    age,
    income,
    home,
    employmentLength,
    intent,
    loanAmount,
    interestRate,
  };

  console.log(JSON.stringify(loan));

  // Forward the data to the external server
  fetch('http://192.168.43.195:5000/predict-model', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(loan),
  })
  .then(response => response.json())
  .then(data => {
    console.log('Response from external server:', data);
    res.render("index", { error: "" }); // Optionally render the result in the same view
  })
  .catch(error => {
    console.error('Error:', error);
    res.render("index", { error: "An error occurred while processing your request." });
  });
});


app.listen(3000, () => {
  console.log("Server is running on port 3000");
});




// app.post("/http://192.168.43.195:5000/predict-model", (req, res) => {
//   const { name, age, income, home, employmentLength, intent, loanAmount, interestRate } = req.body;

//   if (!name || !age || !income || !home || !employmentLength || !intent || !loanAmount || !interestRate) {
//     let error = "All fields are required.";
//     return res.render("index", { error });
//   }

//   const loan = {
//     name,
//     age,
//     income,
//     home,
//     employmentLength,
//     intent,
//     loanAmount,
//     interestRate,
//   };

//   console.log(JSON.stringify(loan));
  
//   res.render("index", { error: "" });
// });

