from django.shortcuts import render
from django.http import HttpResponse
from .forms import ApprovalForm
import numpy as np
import pickle
import os
import pandas as pd


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))

preprocessor_path = os.path.join(project_root, 'preprocessor.pkl')
with open(preprocessor_path, 'rb') as f:
    preprocessor = pickle.load(f)

xgb_model_path = os.path.join(project_root, 'xgb_model.pkl')
with open(xgb_model_path, 'rb') as f:
    xgb_model = pickle.load(f)

# Create your views here.
def hello(request):
    return HttpResponse('Hello, World!')

def index(request):
    form = ApprovalForm()
    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            form.save()
            # Retrieving String Values 
            education = str(form.cleaned_data['education']).strip()
            emplyement_status = str(form.cleaned_data['emplyement_status']).strip()

            # Retrieving Int64 Values
            dependents = np.int64(form.cleaned_data['dependents'])
            income = np.int64(form.cleaned_data['income'])
            credit_score = np.int64(form.cleaned_data['credit_score'])
            loan_amount = np.int64(form.cleaned_data['loan_amount'])
            loan_term = np.int64(form.cleaned_data['loan_term'])
            resident_asset = np.int64(form.cleaned_data['resident_asset'])
            commercial_asset = np.int64(form.cleaned_data['commercial_asset'])
            luxury_asset = np.int64(form.cleaned_data['luxury_asset'])
            bank_asset = np.int64(form.cleaned_data['bank_asset'])

            input_data = {
                'no_of_dependents': dependents,
                'education': education,
                'self_employed': emplyement_status,
                'income_annum': income,
                'loan_amount': loan_amount,
                'loan_term': loan_term,
                'residential_assets_value': resident_asset,
                'commercial_assets_value': commercial_asset,
                'luxury_assets_value': luxury_asset,
                'bank_asset_value': bank_asset,
                'amount_by_income': loan_amount/income,
                'risk_score': -np.log(loan_amount/ (income/12 *loan_term)),
                'mean_asset_value': (resident_asset+commercial_asset+luxury_asset+bank_asset)/4,
                'credit_score': credit_score,
            }

            input_df = pd.DataFrame([input_data])

            scaled_input = preprocessor.transform(input_df)
            input_proba = xgb_model.predict_proba(scaled_input)[:, 1]

            threshold = 0.5

            print(input_proba)
            if input_proba[0] >= threshold:
                return render(request, 'success.html')
            else:
                return render(request, 'failure.html')
            
    return render(request, 'index.html', {'form': form})