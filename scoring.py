def calculate_score(features):
    """
    Calculate a quality score based on the extracted features.
    :param features: List of features in the order:
        [num_sections, has_viewport, content_length, num_images,
        num_links, num_headings, text_to_html_ratio, has_meta_description, title_length]
    :return: Quality score as an integer.
    """
    score = 0
    
    # Scoring rules
    if features[0] > 10:  # num_sections
        score += 10
    else:
        score += 5
    
    if features[1]:  # has_viewport
        score += 20
    else:
        score -= 20
    
    if features[2] > 10000:  # content_length
        score += 15
    else:
        score += 5
    
    if features[3] > 10:  # num_images
        score += 10
    else:
        score += 5
    
    if features[4] > 50:  # num_links
        score += 10
    else:
        score += 5
    
    if features[5] > 5:  # num_headings
        score += 10
    else:
        score += 5
    
    if features[6] > 0.5:  # text_to_html_ratio
        score += 10
    else:
        score += 5
    
    if features[7]:  # has_meta_description
        score += 15
    else:
        score -= 15
    
    if 50 <= features[8] <= 70:  # title_length
        score += 10
    else:
        score += 5
    
    return score

def categorize_score(score):
    """
    Categorize the score into a quality level.
    :param score: Integer score.
    :return: String category.
    """
    if score >= 80:
        return "High Quality"
    elif 50 <= score < 80:
        return "Medium Quality"
    else:
        return "Low Quality"
