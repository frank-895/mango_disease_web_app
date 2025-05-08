def generate_plan(user):
    from datetime import date

    orchards = Orchard.objects.filter(user=user)
    today = date.today()
    plan = []

    for orchard in orchards:
        records = Record.objects.filter(orchardID=orchard).order_by('-recordedAt')
        last_record = records.first()

        if not last_record:
            last_check_days = 30  # Assume high risk if never checked
        else:
            last_check_days = (today - last_record.recordedAt).days

        # Example values (normally you'd calculate or query these)
        disease = last_record.disease
        severity = disease.severity / 10
        spreadability = disease.spreadability / 10

        # Normalize other factors
        variety_sus = VarietyDisease.objects.filter(variety=orchard.variety, disease=disease).first()
        location_sus = LocationDisease.objects.filter(location=orchard.location, disease=disease).first()
        variety_score = variety_sus.varietySusceptability / 10 if variety_sus else 0
        location_score = location_sus.locationSusceptability / 10 if location_sus else 0

        stocking_rate = (orchard.noTreesRow * orchard.noTreesColumn) / orchard.area
        stocking_score = min(stocking_rate / 10, 1)

        last_check_score = min(last_check_days / 30, 1)

        # Weighted sum
        risk_score = (
            0.25 * severity +
            0.2 * spreadability +
            0.15 * variety_score +
            0.15 * location_score +
            0.1 * stocking_score +
            0.15 * last_check_score
        )

        # Determine frequency
        if risk_score > 0.7:
            frequency = "Every 3 days"
        elif risk_score > 0.4:
            frequency = "Every 7 days"
        else:
            frequency = "Every 14 days"

        plan.append({
            'orchard': orchard.orchardName,
            'risk_score': round(risk_score, 2),
            'recommended_check_frequency': frequency
        })

    return plan
