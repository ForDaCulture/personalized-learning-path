def recommend_path(grade, learning_style):
    # Determine module level based on grade
    if grade > 80:
        level = "Advanced"
    elif grade > 60:
        level = "Intermediate"
    else:
        level = "Basic"
    
    # Determine module type based on learning style
    if learning_style == "visual":
        content = "Video Lessons"
    elif learning_style == "auditory":
        content = "Audio Lessons"
    else:
        content = "Text Lessons"
    
    return {'level': level, 'type': content}