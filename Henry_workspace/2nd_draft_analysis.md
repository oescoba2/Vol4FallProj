## 2nd Draft Analysis

Our model demonstrates that ODEs are a promising way to model breast cancer growth.
The predicted effect specifically of chemotherapy is appealing. 


When we examine the parts of our model, the most promising is the model of chemotherapy alone. 
Our model predicts, as a expected, that a single round of chemotherapy strongly weakens a tumor in the first few days before the tumor rebounds. 
Without the immune response, though, no number of chemotherapy treatments protects against the tumor growing exponentially after the last treatment.

Our full model succesfully kills cancer after the last treatment, but the immune system component of the model remains a weak point. 
The immune system model on its own performs poorly in the long term.
It experiences discontinuities and negative cell populations after only 30 days.
Initial conditions also highly affect the results of the immune model.
When we integrate the immune system into our full model, we mitigate a lot of negative consequences by inhibiting immune cells with chemotherapy.
However, our immune system equations still contribute to our model's sensitivity to inital conditions.
The sensitivity of our immune equations also casts doubt on whether our model accurately predicts the death of cancer cells after chemotherapy.

Another weakness of our model is the uncertainty of our parameters.
Most of these parameters were found experimentally, but with different experiments under varying assumptions.
Moreover, when we introduced a parameter to our final model to ihibit immune response due to chemotherapy, we simply chose a value which produced convincing qualitative results.
Fully inspecting and adjusting our parameters would be difficult, but would make our model more quantitatively correct.

Several simplifying assumptions also weaken our model. 
First of all, unlike other attempts to model tumor burden, we did not consider normal cells in the area with cancer.
Including normal cells could drastically affect the dynamics of our model.
Secondly, we modeled chemotherapy with a single drug that affects all cancer cells.
Typically, chemotherapy involves several drgus which affect cancer cells in different stages.
Finally, our full model includes a term which indicates that chemotherapy kills immune cells.
Typically, chemotherapy only inihibts immune cells, but since we model immune cell population, that information is hard to incorporate.

If our model accurately predicted tumor burden, it might be useful to prescribe chemotherapy treatments to breast cancer patients. 
Given initial measurements of tumor burden and immune cells, doctors could predict whether a patient is in remission and corroborate the patient's symptoms with the tumor growth model. 
However, currently, our model does not predict results without chemotherapy well.
If our model is to be useful, it needs to accurately predict tumor burden in the absence of chemotherapy or after chemotherapy treatments.
Given more time, we might futher inspect whether the model accurately predicts outcomes given insufficient treatment and alter our parameters.
