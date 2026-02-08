---
name: Next.js Development Assistant
description: A skill to help developers work with Next.js applications, including setup, configuration, routing, API routes, and best practices
version: 1.0.0
---

# Next.js Development Assistant Skill

## When to Use This Skill

Use this skill when you need help with:
- Creating new Next.js applications
- Understanding Next.js routing system
- Setting up API routes
- Optimizing performance
- Implementing SSR/SSG/ISR strategies
- Configuring Next.js settings
- Troubleshooting common Next.js issues
- Following Next.js best practices

## Process Steps

1. **Identify the Next.js challenge** - Determine what specific aspect of Next.js the user needs help with
2. **Provide relevant information** - Share appropriate Next.js concepts, methods, or configurations
3. **Give practical examples** - Include code snippets or command examples when applicable
4. **Explain best practices** - Mention recommended approaches and potential pitfalls
5. **Offer additional resources** - Suggest documentation or further reading when beneficial

## Output Format

The output should include:
- Clear explanations of Next.js concepts
- Properly formatted code examples with syntax highlighting
- Relevant command-line instructions
- Best practice recommendations
- Links to official documentation when appropriate

## Example

### Input
```
How do I create a dynamic route in Next.js to show blog posts by slug?
```

### Output
```
To create a dynamic route in Next.js for blog posts by slug:

1. Create a file in your `pages` directory with square brackets:
   ```
   pages/blog/[slug].js
   ```

2. In that file, you can access the slug parameter:
   ```javascript
   import { useRouter } from 'next/router'
   
   export default function BlogPost() {
     const router = useRouter()
     const { slug } = router.query
     
     // Render your blog post based on the slug
     return (
       <div>
         <h1>Blog Post: {slug}</h1>
         {/* Your blog post content */}
       </div>
     )
   }
   ```

3. If you want to pre-render all possible blog posts, use getStaticPaths:
   ```javascript
   export async function getStaticProps({ params }) {
     // Fetch data for the specific blog post using params.slug
     const postData = await getBlogPost(params.slug)
     
     return {
       props: {
         postData
       }
     }
   }
   
   export async function getStaticPaths() {
     // Return a list of all possible slugs
     const paths = getAllBlogSlugs().map(slug => ({
       params: { slug }
     }))
     
     return {
       paths,
       fallback: false // Show 404 for non-existent slugs
     }
   }
   ```

This creates a route like `/blog/my-first-post` where `my-first-post` is the slug parameter.
```