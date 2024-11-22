The fully integrated cancer model with both chemotherapy and immune cells predicts unreasonable results for chemotherapy without additional adjustments. For reasonable initial tumor sizes, one or two rounds of chemotherapy almost immediately kill the tumor. In practice, patients undergo 5-8 rounds of chemotherapy on average before showing signs of remission [CITE!!]. Such problematic behavior is likely a result of the immune model, which as presented in a previous paper does not generalize well past 30 days. Thus, we tweaked our initial full model to produce qualitatively sound results.

[Plot of tumor burden for full model without last term in immune cell equations]

In order to fix the full tumor growth model qualitatively, we introduced a term in the differential equations for both CD8 cells and natural killer cells. Scientific papers have produced different conclusions on whether chemotherapy inhibits CD8 and natural killer cells[CITE], but we chose to incorporate a term which inhibits CD8 and natural killer cells in proportion to their interactions with the chemotherapy drug. We altered this new parameter until simulations prediction at least 5 rounds of chemotherapy before remittance. 


