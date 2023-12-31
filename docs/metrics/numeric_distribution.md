# **Numeric Distribution Metrics**

Numeric Distribution metrics detect changes in the numeric distribution of values, including outliers, variance, skew and more


## **Average**

Average metrics gauge performance in transitional databases and search engines, offering valuable insights into overall effectiveness.


**Example**

```yaml title="dcs_config.yaml"
metrics:
  - name: avg_price
    metric_type: avg
    resource: product_db.products.price
    filters:
      where: "country_code = 'IN'"
    validation:
      threshold: "< 190"
```


## **Minimum**

Minimum metrics ensure consistency across transitional databases and search engines, enhancing data quality and retrieval accuracy.

**Example**

```yaml title="dcs_config.yaml"
metrics:
  - name: min_price
    metric_type: min
    resource: product_db.products.price
    validation:
      threshold: "> 0"
```

## **Maximum**

Maximum metrics gauge the highest values within datasets, helping identify outliers and understand data distribution's upper limits for quality assessment.

**Example**

```yaml title="dcs_config.yaml"
metrics:
  - name: max_price
    metric_type: max
    resource: product_db.products.price
    validation:
      threshold: "< 1000"
```

```yaml title="dcs_config.yaml"
- name: max_price_of_products_with_high_rating
  metric_type: max
  resource: product_db.products.price
  filters:
    where: "rating > 4"
  validation:
    threshold: "< 1000"
```

## **Sum**

Sum metrics measure the total of all values within a dataset, indicating the overall size of a particular dataset to help understand data quality.

**Example**

```yaml title="dcs_config.yaml"
metrics:
  - name: sum_of_price
    metric_type: sum
    resource: product_db.products.price
    validation:
      threshold: "> 100 & < 1000"
```

## **Variance**

Variance in data quality measures the degree of variability or dispersion in a dataset, indicating how spread out the data points are from the mean.

**Example**

```yaml title="dcs_config.yaml"
metrics:
- name: variance_of_price
  metric_type: variance
  resource: product_db.products.price
```

## **Standard Deviation**

Standard deviation metrics measure the amount of variation or dispersion of a set of values from the mean, indicating how spread out the data points are from the mean.

**Example**

```yaml title="dcs_config.yaml"
metrics:
- name: standard_deviation_of_price
  metric_type: stddev
  resource: product_db.products.price
```

## **Skew**
**Coming Soon..**

## **Kurtosis**
**Coming Soon..**

## **Geometric Mean**
**Coming Soon..**

## **Harmonic Mean**
**Coming Soon..**