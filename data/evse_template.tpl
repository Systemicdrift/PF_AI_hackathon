{
  "receiver": "axcess",
  "status": "resolved",
  "alerts": [
    {
      "status": "firing",
      "labels": {
        "acc_id": "021",
        "acg_id": "03",
        "acn_id": "0086",
        "acs_id": "05",
        "alertname": "EVSE Faulty Charger",
        "consumer": "axcess",
        "evse_type": "Webasto DX",
        "instance": "netflix.powerflex.com:9001",
        "job": "netflix",
        "receive": "true",
        "severity": "critical",
        "space_number": "EV#6",
        "state": "FAULTY CHARGER",
        "team": "hit",
        "tenant_id": "default-tenant",
        "version": "v1"
      },
      "annotations": {
        "derType": "EVSE",
        "description": "EVSE is reporting faulty charger status",
        "summary": "EVSE has entered FAULTY CHARGER state"
      },
      "startsAt": "2023-03-06T16:52:14.957445121Z",
      "endsAt": "2000-03-06T16:52:14.957445121Z",
      "generatorURL": "/graph?g0.expr=job%3Acount_evse_state%3Afaulty_charger\u0026g0.tab=1",
      "fingerprint": "23423423423"
    },
    {
      "status": "resolved",
      "labels": {
        "acc_id": "02",
        "acg_id": "03",
        "acn_id": "0086",
        "acs_id": "05",
        "alertname": "EVSE Faulty Charger",
        "consumer": "axcess",
        "evse_type": "Webasto DX",
        "instance": "netflix.powerflex.com:9001",
        "job": "netflix",
        "receive": "true",
        "severity": "critical",
        "space_number": "EV#6",
        "state": "FAULTY CHARGER",
        "team": "hit",
        "tenant_id": "default-tenant",
        "version": "v1"
      },
      "annotations": {
        "derType": "EVSE",
        "description": "EVSE is reporting faulty charger status",
        "summary": "EVSE has entered FAULTY CHARGER state"
      },
      "startsAt": "2023-02-08T17:52:14.957445121Z",
      "endsAt": "2023-02-08T17:54:14.957445121Z",
      "generatorURL": "/graph?g0.expr=job%3Acount_evse_state%3Afaulty_charger\u0026g0.tab=1",
      "fingerprint": "d0e85f29fbde9bdd88333"
    },
    {
      "status": "resolved",
      "labels": {
        "acc_id": "130",
        "acn_id": "0007",
        "alertname": "V2 Sites offline metric",
        "consumer": "axcess",
        "severity": "critical",
        "team": "hit"
      },
      "annotations": {
        "derType": "SITE",
        "description": "V2 Sites offline",
        "summary": "Offline V2 Sites due to interruption of up metric reporting"
      },
      "startsAt": "2023-02-06T15:52:14.957445121Z",
      "endsAt": "0001-01-01T00:00:00Z",
      "generatorURL": "/graph?g0.expr=job%3Av2sitesList%3Av2sites_reporting&g0.tab=1",
      "fingerprint": "f0c999b2bd0ee34c"
    }
  ],
  "groupLabels": { "job": "netflix" },
  "commonLabels": {
    "acc_id": "02",
    "acg_id": "03",
    "acn_id": "None",
    "acs_id": "05",
    "alertname": "EVSE Faulty Charger",
    "consumer": "axcess",
    "evse_type": "Webasto DX",
    "instance": "netflix.powerflex.com:9001",
    "job": "netflix",
    "receive": "true",
    "severity": "critical",
    "space_number": "EV#6",
    "state": "FAULTY CHARGER",
    "team": "hit",
    "tenant_id": "default-tenant",
    "version": "v1"
  },
  "commonAnnotations": {
    "derType": "EVSE",
    "description": "EVSE is reporting faulty charger status",
    "summary": "EVSE has entered FAULTY CHARGER state"
  },
  "externalURL": "http://alertmanager-alertmanager-0:9093",
  "version": "4",
  "groupKey": "{}/{consumer=\"axcess\"}:{job=\"netflix\"}",
  "truncatedAlerts": 0
}