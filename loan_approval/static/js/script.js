const loanPurpose = document.getElementById('loan-purpose-id')
const loanTerm = document.getElementById('loan-term-id')

const loanPerPurpose = {
    // student loan
    'Education': [12, 24, 36, 48, 60, 84, 120],
    // medical loan 
    'Medical': [6, 12, 24, 36, 48],
    // venture loan 
    'Venture': [6, 12, 24, 36],
    // personal loan 
    'Personal': [12, 24, 36, 48, 60],
    // debt consolidation 
    'DebtConsolidation': [24, 36, 48, 60],
    // home improvement
    'HomeImprovement': [12, 24, 36, 48, 60, 84]
}

updateLoanTerms('Education')

loanPurpose.addEventListener('change', () => {
    const selectedValue = loanPurpose.value
    updateLoanTerms(selectedValue)
})
function updateLoanTerms(purposeKey){
    loanTerm.replaceChildren()
    loanPerPurpose[purposeKey].forEach((term) => {
        const option = document.createElement('option')
        option.value = String(term)
        option.textContent = `${term} Months`
        loanTerm.appendChild(option)
    })
}

const my_transfered_ds = {
    'person_age': document.getElementById('age-id').value,
    'person_gender': document.getElementById('gender-id').value,
    'person_education': document.getElementById('education-id').value,
    'person_income': document.getElementById('income-id').value,
    'person_emp_exp': document.getElementById('job-yr-id').value,
    'person_home_ownership': document.getElementById('housing-status-id').value,
    'loan_amnt': document.getElementById('loan-amm-id').value,
    'loan_intent': document.getElementById('loan-purpose-id').value,
    'loan_percent_income': (document.getElementById('loan-amm-id').value)/(document.getElementById('income-id').value),
    'cb_person_cred_hist_length': document.getElementById('cred-hist-id').value,
    'credit_score': document.getElementById('cred-score-id').value,
    'previous_loan_defaults_on_file': document.getElementById('default-loan-id').value,
}
    
console.log(my_transfered_ds);  // Ensure values are not undefined/NaN
console.log(JSON.stringify(my_transfered_ds));  // Should be valid JSON

fetch('http://127.0.0.1:5000/result', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',  // Must be exactly this
    },
    body: JSON.stringify(my_transfered_ds)  // Ensure data is stringified
})
.then(response => response.json())
.then(data => console.log(data))

