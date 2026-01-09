# Overview

This codebase contains the models for a website. It includes models for blog posts, video content, gallery images, team members, company details, SEO settings, and appointment requests.

## Models

### BlogPost

- `title`: CharField, the title of the blog post
- `slug`: SlugField, the URL-friendly version of the title
- `content`: TextField, the content of the blog post
- `author`: ForeignKey, the author of the blog post
- `created_at`: DateTimeField, the date and time the blog post was created
- `updated_at`: DateTimeField, the date and time the blog post was last updated

### VideoContent

- `title`: CharField, the title of the video content
- `embedded_url`: TextField, the URL or embed code for the video content
- `platform`: CharField, the platform on which the video content is hosted (TikTok or YouTube)
- `processed_id`: CharField, the processed ID of the video content (e.g., YouTube video ID or TikTok video ID)
- `created_at`: DateTimeField, the date and time the video content was created

### GalleryImage

- `title`: CharField, the title of the gallery image
- `image`: ImageField, the image file for the gallery image
- `alt_text`: CharField, the alternative text for the gallery image
- `created_at`: DateTimeField, the date and time the gallery image was created

### TeamMember

- `name`: CharField, the name of the team member
- `role`: CharField, the role of the team member
- `bio`: TextField, the biography of the team member
- `image`: ImageField, the image file for the team member

### Company

- `full_name`: CharField, the full name of the company
- `short_name`: CharField, the short name of the company

### SEOTitleAndMetaDescription

- `page_type`: CharField, the type of page the SEO data belongs to
- `title`: CharField, the SEO title for the page
- `meta_description`: TextField, the SEO meta description for the page

### Appointment

- `name`: CharField, the name of the person making the appointment request
- `email`: EmailField, the email address of the person making the appointment request
- `phone`: CharField, the phone number of the person making the appointment request
- `message`: TextField, the message or additional information provided by the person making the appointment request
- `status`: CharField, the status of the appointment request (pending, confirmed, completed, cancelled)
- `admin_notes`: TextField, any additional notes or comments added by the admin
- `created_at`: DateTimeField, the date and time the appointment request was created
- `updated_at`: DateTimeField, the date and time the appointment request was last updated

## Proxies

### NewRequest

A proxy model for the `Appointment` model, specifically for new appointment requests.

### CompletedRecord

A proxy model for the `Appointment` model, specifically for completed appointment records.

## Usage

To use these models in your Django project, you can import them into your code and use them as you would with any other Django model. For example, to create a new blog post, you can do the following:
