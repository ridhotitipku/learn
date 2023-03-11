products = [
    'buy_saham_transaction_amount',
    'buy_pasar_uang_transaction_amount',
    'buy_pendapatan_tetap_transaction_amount',
    'buy_campuran_transaction_amount',
]

count_buy_product = []


for product in products:
    df_product = df_eda[df_eda[product] != 0]

    print(product)
    segmentation = df_product.groupby('income_range')['user_id'].count()
    segmentation = segmentation.reset_index() 
    segmentation
    plt.pie(segmentation['user_id'], labels = segmentation['income_r