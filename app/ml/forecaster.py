from prophet import Prophet
import pandas as pd

def forecast_expenses(transactions):
    if not transactions:
        return {'message': 'No data to forecast'}

    df = pd.DataFrame(transactions)
    df['ds'] = pd.to_datetime(df['date'])
    df['y'] = df['amount']

    # Aggregate weekly
    df = df.groupby(pd.Grouper(key='ds', freq='W'))['y'].sum().reset_index()

    model = Prophet(changepoint_prior_scale=0.05)
    model.fit(df)

    future = model.make_future_dataframe(periods=4, freq='W')
    forecast = model.predict(future)

    forecast['yhat'] = forecast['yhat'].clip(lower=0)

    next_point = forecast[['ds', 'yhat']].tail(1).to_dict(orient='records')[0]
    return next_point
