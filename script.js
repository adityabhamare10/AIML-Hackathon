document.getElementById('submit').addEventListener('click', function(event) {
    event.preventDefault();

    const formData = {
        // name: document.getElementById('name').value,
        age: parseInt(document.getElementById('age').value),
        income: parseInt(document.getElementById('income').value),
        loanAmount: parseInt(document.getElementById('loanAmount').value),
        creditScore: parseInt(document.getElementById('creditScore').value),
        monthsEmployed: parseInt(document.getElementById('monthsEmployed').value),
        numCreditLines: parseInt(document.getElementById('numCreditLines').value),
        interestRate: parseFloat(document.getElementById('interestRate').value),
        loanTerm: parseInt(document.getElementById('loanTerm').value),
        dtiRatio: parseFloat(document.getElementById('dtiRatio').value),
        education:  parseInt(document.getElementById('education').value),
        employmentType:  parseInt(document.getElementById('employmentType').value),
        maritalStatus:  parseInt(document.getElementById('maritalStatus').value),
        hasMortgage:  parseInt(document.getElementById('hasMortgage').value),
        hasDependents:  parseInt(document.getElementById('hasDependents').value),
        loanPurpose:  parseInt(document.getElementById('loanPurpose').value),
        hasCoSigner:  parseInt(document.getElementById('hasCoSigner').value),
    };

    fetch('http://192.168.43.195:5000/predict-model', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response =>  data = response.json())
    .then(data => {
        document.getElementById('prediction').textContent = data.prediction;
        document.getElementById('probability').textContent = JSON.stringify(data.probability, null, 2);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
